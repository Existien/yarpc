/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.2_primitives.yml
 *   Object: Primitives
 *   Template: qt6/service_source.j2
 */
#include "PrimitivesInterfaceAdaptor.hpp"

using namespace gen::with_args;

PrimitivesInterfaceAdaptor::PrimitivesInterfaceAdaptor(PrimitivesInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

uchar PrimitivesInterfaceAdaptor::Uint8Method(
    uchar value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleUint8MethodCalled(_message);
    return {};
}

bool PrimitivesInterfaceAdaptor::BoolMethod(
    bool value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleBoolMethodCalled(_message);
    return {};
}

short PrimitivesInterfaceAdaptor::Int16Method(
    short value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleInt16MethodCalled(_message);
    return {};
}

ushort PrimitivesInterfaceAdaptor::Uint16Method(
    ushort value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleUint16MethodCalled(_message);
    return {};
}

int PrimitivesInterfaceAdaptor::Int32Method(
    int value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleInt32MethodCalled(_message);
    return {};
}

uint PrimitivesInterfaceAdaptor::Uint32Method(
    uint value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleUint32MethodCalled(_message);
    return {};
}

qlonglong PrimitivesInterfaceAdaptor::Int64Method(
    qlonglong value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleInt64MethodCalled(_message);
    return {};
}

qulonglong PrimitivesInterfaceAdaptor::Uint64Method(
    qulonglong value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleUint64MethodCalled(_message);
    return {};
}

double PrimitivesInterfaceAdaptor::DoubleMethod(
    double value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleDoubleMethodCalled(_message);
    return {};
}

QString PrimitivesInterfaceAdaptor::StringMethod(
    QString value,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleStringMethodCalled(_message);
    return {};
}

